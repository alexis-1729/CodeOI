<?php

namespace Config;

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes -> setDefaultNamespace('App\Controllers');

$routes = Services::routes();

$routes->get('/', 'Home::index');
$routes -> setTranslateURIDashes(false);
$routes -> set404Override();
$routes ->setAutoRoute(true);
