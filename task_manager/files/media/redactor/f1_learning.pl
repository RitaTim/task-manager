package App::Admin::Learning;
use App::Base -controller;
use Data::Dumper;

#has collection => sub { shift->mongo->get_collection('article') };

sub main {
    my $self  = shift;
    ###################################################
    my $articles = [$self->mongo->get_collection('article')->find({'$or' => [{deleted => 0}, {deleted => undef}] })->all ];
    $self->render(articles => $articles);
}

sub edit {
    my $self = shift;
    my $time = time;
    
    if ( $self->param('submit') ) {
        unless ( $self->param('id') ) { #add article
            #########################################
            my $last_position = scalar $self->mongo->get_collection('article')->find( { '$or' => [{deleted => 0}, {deleted => undef}] } )->fields({position => 1})->all;
            $self->mongo->get_collection('article')->insert({
                    (map { $_ => $self->param($_) || '' } qw(title text)),
                    (map { $_ => $time } qw(updated created)),
                    hidden => $self->param('hidden') ? 1 : 0,
                    position => $last_position + 1,
                    
            });
        } else {     #edit article
            $self->mongo->get_collection('article')->update(
                    { _id => $self->oid( $self->param('id') ) },
                    ############################################
                    { '$set' => {
                            (map { $_ => $self->param($_) || '' } qw(title text)),
                            hidden => $self->param('hidden') ? 1 : 0,
                            updated => $time,
                        }
                    }
            );
        }
        $self->redirect('/admin/learning');
    } else {
        if ($self->param('id') ){
            my $article = $self->mongo->get_collection('article')->find_one({ _id => $self->oid($self->param('id')) });
            $self->render( article => $article);
        }
    }
}

############################
sub delete {
    my $self = shift;
    my $where->{_id} = $self->oid($self->param('id'));
    
    $self->mongo->get_collection('article')->update(
                    { _id => $self->oid( $self->param('id') ) },
                    { '$set' => {
                            position => -1,
                            deleted => 1
                        }
                    }
    );

    my $id_moved_articles = [ $self->mongo->get_collection('article')->finde({ "gt" => { position => $self->param('position') })->fields( { _id => 1 } )->all];
    $self->_moved_articles($id_moved_articles, -1);

    $self->redirect('/admin/learning');
    #$self->render(json => {ok => 1});
}

##################################
sub change_order {
    ($self, $id, $from_position, $to_position, $direction) = shift;
    my $moved_positions = $direction eq "back" ? [$to_position..$from_position - 1] : [$from_position + 1..$to_position];
    my $step            = $direction eq "back" ? 1 : -1;
    my $id_moved_articles = [$self->mongo->get_collection('article')->find({position => {'$in' => $moved_positions }})->fields({_id=>1})->all ];
    $self->_moved_articles($id_moved_articles, $step);

    $self->mongo->get_collection('article')->update(
                    { _id => $self->oid($id) },
                    { 
                        '$set' => {
                            position => $to_position
                        }
                    }
            );
}

###########################################
sub change_status{
    my $self = shift;
    $self->mongo->get_collection('article')->update(
                    { _id => $self->oid( $self->param('id') ) },
                    { 
                        '$set' => {
                            hidden => $article->{hidden} ? 0 : 1,
                            updated => time,
                        }
                    }
            );
}

#########################
sub _moved_articles{
    my ($self, $id_mpved_articles, $step) = @_;
}

############################
sub list {
    my $self  = shift;
    my $articles = [$self->mongo->get_collection('article')->find({ '$and' => [ 
            {
                '$or' => [
                    {deleted => 0}, 
                    {deleted => undef}
                ]
            },
            {
               hidden => 0
            }
    ] } )->all ];

    $self->render(json => { articles => $articles});
}

sub article {
    my $self  = shift;
    my $article = $self->mongo->get_collection('article')->find_one({ _id => $self->oid($self->param('id')) });
    $self->render(json => { article => $article});
}

###############################3
sub last_updated {
    my $self = shift;
    my $last_updated = [$self->mongo->get_collection('article')->find({ '$and' => [ 
            {
                '$or' => [
                    {deleted => 0}, 
                    {deleted => undef}
                ]
            },
            {
               hidden => 0
            }
    ] } )->fields({updated => 1})->sort({updated => -1})->all]->[0];
    $self->render(json => { last_updated => $last_updated->{updated}}); 
}

1;







	$admin->get('/learning')->to('admin-learning#main')->name('admin_learning');	
    $admin->route('/learning/add')->to('admin-learning#edit', add => 1)->name('admin_edit');
######################
    $admin->route('/learning/delete/:id/:position')->to('admin-learning#delete');      
    $admin->get('/learning/change_status/:id')->to('admin-learning#change_status');
    $admin->get('/learning/change_order')->to('admin-learning#change_order');
###API
    $admin->get('/learning/list')->to('admin-learning#list');
    $admin->get('/learning/article/:id')->to('admin-learning#article');

	$admin->get('/learning/last_updated')->to('admin-learning#last_updated');
    	
    
    $admin->route('/learning/save/:id')->to('admin-learning#edit')->name('admin_edit');
	$admin->route('/learning/:id')->to('admin-learning#edit')->name('admin_edit');









