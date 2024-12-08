<?php
namespace App\Controllers;

class Arena extends BaseController{
    public function index(){
        return view('header')
        .view('arena/arena')
        .view('footer');
    }
}


?>