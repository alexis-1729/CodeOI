<?php
namespace App\Controllers;


class Secciones extends BaseController
{
    public function introduccion(){
        return view('header')
        .view('secciones/introductorio')
        .view('footer');
    }

    public function basico(){
        return view('header')
        .view('secciones/basico')
        .view('footer');
    }

    public function intermedio(){
        return view('header')
        .view('secciones/intermedio')
        .view('footer');
    }

    public function avanzado()
    {
        return view('header')
        .view('secciones/avanzado')
        .view('footer');
    }

}
?>