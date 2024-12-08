<?php
namespace App\Controllers;

class Acercade extends BaseController
{
    public function index(){
            return view('header')
            .view('acerca de/acercade')
            .view('footer');
    }

}


?>