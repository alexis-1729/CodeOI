<?php

namespace Config;

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */

 $routes = Services::routes();
$routes -> setDefaultNamespace('App\Controllers');
$routes -> setTranslateURIDashes(false);
$routes -> set404Override();
$routes->get('/', 'Home::index');
$routes ->setAutoRoute(true);
