<?php

namespace App\Controllers;

use App\Models\LoginModel;

class Login extends BaseController
{
    protected $user;
    protected $reglasR;
    protected $reglas;
    protected $sesion;
     public function __construct()
     {
        
         $this->user = new LoginModel();
         $this->sesion=session();
         helper(['form']);

        //  reglas login
         $this->reglasR = [
             'usuario'=> [
                     'rules' => 'required',
                     'errors' => [
                     'required' =>'El campo {field} es obligatorio',
                     ]
                     ],
             'password'=> [
                 'rules' => 'required',
                'errors' => [
                    'required' =>'El campo {field} es obligatorio',
                ]
                ]
        ];

        // reglas registro
        $this->reglas = [
                   
            'user'=>  'required|min_length[3]',
                    
            'email'=>  'required|valid_email|is_unique[info_user.user_correo]',
                    
                    
            'password'=>  'required|min_length[8]|max_length[20]',
              
              'repassword'=>  'required|matches[password]',   
        ];
     }

    public function index()
    {
        echo view('login/login');
    }

    public function logear(){
        if($this -> request->getMethod() == 'POST' && $this->validate($this ->reglasR)){
            $usuario = $this->request->getVar('user');
            $password = $this->request->getVar('password');

            $datos = $this->user->where('user_username', $usuario)->first();
            if($datos != null){
                if(password_verify($password, $datos['user_password'])){
                    $datosSesion =[
                        'user_correo'=>$datos['user_correo'],
                        'user_usuario' => $datos['user_username']
                       ];
                       $session = session();
                       $session ->set($datosSesion);
                       return redirect()->to(base_url());


                }else{
                    $data['error'] = 'La constraseña no coincide';
                    return view('login/login', $data);
                }
            }
        }
    }

    public function registro(){
        return view('login/registro');
    }

    public function registrar(){
        if($this->request->getMethod() == 'POST'){
            if($this->validate($this->reglas)){
            $hash = password_hash($this->request->getVar('password'),PASSWORD_DEFAULT);
            $this-> user ->save([ 
                'user_correo' => $this->request->getVar('email'), 
                'user_username' => $this->request->getVar('user'), 
                'user_password' => $hash]);
            $data = array(
                'username' => $this->request->getVar('user'),
                 'user_email' => $this->request->getVar('email'),
            );
            $session = session();
            $session ->set($data);
            $response = array(
                'status' => 'success',
                'message' => 'registro exitoso'
            );
            }else{
                $response = array(
                    'status' => 'error',
                    'message' => 'registro fallido'
                );
                $data =['validation' => $this->validator];
            return view('login/login', $data);
            }
        }else{
            $response = array(
                'status' => 'error',
                'message' => 'Error en el metodo post'
            );
        }
        return $this->response->setJSON($response);

    }
    public function logout(){
        $sesion = session();
        $sesion ->destroy();
        return redirect()->to(base_url());
    }
}
