#from datetime import date


class Cliente(object):
    
    
    def __init__(self):
        pass
    # def __init__(self, nu_cliente: int, cd_pais:int, cd_canal:str ,cd_sucursal:str , nu_folio:int ,id_icu_bazdig:int ,id_superapp:int , nb_ap_paterno:str,
    #             nb_ap_matern:str, nb_nombre:str , tp_persona:str ,nu_telefono:int, nb_genero:str, fh_nacimiento:date, nb_nacionalidad:str ,nb_curp:str, nb_rfc:str ,
    #             nb_e_mail:str ,nb_dir_calle:str , nb_dir_numero:int ,nb_dir_colonia:str, cd_dir_cp:str ,nb_dir_estado:str ,nb_dir_ciudad:str, 
    #             nb_txt_adr:str ,nb_des_comprcty:str ,fh_alta_cliente: date ,fh_alta_bazdig:date, 
    #             fh_alta_superapp:date, fh_ult_traspasos:date,fh_ult_speis:date, fh_ult_ret_suc:date , fh_ult_qr_caja:date,
    #             fh_ult_qr_atm: date, fh_ult_mod_dermo:date, fh_mod_email:date, 
    #             fh_mod_telefono:date,fh_mod_biometricos:date,tp_registro:str) -> None:
        
    #     self.__nu_cliente= nu_cliente
    #     self.__cd_pais = cd_pais 
    #     self.__cd_canal =cd_canal
    #     self.__cd_sucursal = cd_sucursal
    #     self.__nu_folio = nu_folio 
    #     self.__nb_dir_calle= nb_dir_calle
    #     self.__id_icu_bazdig = id_icu_bazdig
    #     self.__id_superapp = id_superapp
    #     self.__nb_ap_paterno= nb_ap_paterno
    #     self.__nb_ap_matern= nb_ap_matern
    #     self.__nb_nombre = nb_nombre
    #     self.__tp_persona = tp_persona
    #     self.__nu_telefono= nu_telefono
    #     self.__nb_genero= nb_genero
    #     self.__fh_nacimiento= fh_nacimiento
    #     self.__nb_nacionalidad = nb_nacionalidad
    #     self.__nb_curp= nb_curp
    #     self.__nb_rfc = nb_rfc
    #     self.__nb_e_mail = nb_e_mail
    #     self.__nb_dir_calle =   nb_dir_calle   
    #     self.__nb_dir_numero= nb_dir_numero
    #     self.__nb_dir_colonia = nb_dir_colonia      
    #     self.__cd_dir_cp = cd_dir_cp
    #     self.__nb_dir_estado = nb_dir_estado
    #     self.__nb_dir_ciudad= nb_dir_ciudad
    #     self.__nb_txt_adr = nb_txt_adr
    #     self.__nb_des_comprcty = nb_des_comprcty
    #     self.__fh_alta_cliente = fh_alta_cliente
    #     self.__fh_alta_bazdig= fh_alta_bazdig
    #     self.__fh_alta_superapp= fh_alta_superapp
    #     self.__fh_ult_traspasos= fh_ult_traspasos
    #     self.__fh_ult_speis= fh_ult_speis
    #     self.__fh_ult_ret_suc= fh_ult_ret_suc
    #     self.__fh_ult_qr_caja= fh_ult_qr_caja 
    #     self.__fh_ult_qr_atm =  fh_ult_qr_atm  
    #     self.__fh_ult_mod_dermo= fh_ult_mod_dermo  
    #     self.__fh_mod_email= fh_mod_email
    #     self.__fh_mod_telefono= fh_mod_telefono
    #     self.__fh_mod_biometricos= fh_mod_biometricos
    #     self.__tp_registro= tp_registro
        
        
    @property
    def nu_cliente(self):
        return self.__nu_cliente
    
    @nu_cliente.setter
    def nu_cliente(self, val):
        self.__nu_cliente = val
            
    @property
    def cd_pais(self):
        return self.__cd_pais
    
    @cd_pais.setter
    def cd_pais(self, val):
        self.__cd_pais = val
        
    @property
    def cd_canal(self):
        return self.__cd_canal    
    
    @cd_canal.setter
    def cd_canal(self, val):
        self.__cd_canal= val    
        
    @property
    def cd_sucursal(self):
        return self.__cd_sucursal
    
    @cd_sucursal.setter
    def cd_sucursal(self,val):
        self.__cd_sucursal= val
        
    @property
    def nu_folio(self):
        return self.__nu_folio
    
    @nu_folio.setter
    def nu_folio(self,val):
        self.__nu_folio= val
        
    
    @property
    def nb_dir_calle(self):
        self.__nb_dir_calle
        
    @nb_dir_calle.setter
    def nb_dir_calle(self,val):
        self.__nb_dir_calle= val
            
    @property
    def id_icu_bazdig(self):
        return self.__id_icu_bazdig
    
    @id_icu_bazdig.setter
    def id_icu_bazdig(self,val):
        self.__id_icu_bazdig=val
                                   
    @property
    def id_superapp(self):
        self.__id_superapp
    
    @id_superapp.setter
    def id_superapp(self,val):
        self.__id_superapp=val
    
    @property
    def nb_ap_paterno(self):
        return self.__nb_ap_paterno
    
    @nb_ap_paterno.setter
    def nb_ap_paterno(self, val):
        self.__nb_ap_paterno= val    
    
    @property
    def nb_ap_matern(self):
        return self.__nb_ap_matern 
    
    @nb_ap_matern.setter
    def nb_ap_matern(self, val):
        self.__nb_ap_matern= val
                                              
    @property
    def nb_nombre(self):
        return self.__nb_nombre
    
    @nb_nombre.setter
    def nb_nombre(self, val):
        self.__nb_nombre= val
        
    @property
    def tp_persona(self):
        return self.__tp_persona
    
    @tp_persona.setter
    def tp_persona(self, val):
        self.__tp_persona= val
        
    @property
    def nu_telefono(self):
        return self.__nu_telefono
    
    @nu_telefono.setter
    def nu_telefono(self, val):
        self.__nu_telefono= val
    
    @property
    def nb_genero(self):
        return self.__nb_genero
    
    @nb_genero.setter
    def nb_genero(self, val):
        self.__nb_genero=val
    
    @property
    def fh_nacimiento(self):
        return self.__fh_nacimiento
    
    @fh_nacimiento.setter
    def fh_nacimiento(self, val):
        self.__fh_nacimiento=val
            
    @property
    def nb_nacionalidad(self):
        return self.__nb_nacionalidad            
    
    @nb_nacionalidad.setter
    def nb_nacionalidad(self, val):
        self.__nb_nacionalidad = val
    
    @property
    def nb_curp(self):
        return self.__nb_curp
    
    @nb_curp.setter
    def nb_curp(self, val):
        self.__nb_curp = val
        
    @property
    def nb_rfc(self):
        return self.__nb_rfc
    
    @nb_rfc.setter
    def nb_rfc(self, val):
        self.__nb_rfc = val  
        
    @property
    def nb_e_mail(self):
        return self.__nb_e_mail
    
    @nb_e_mail.setter
    def nb_e_mail(self, val):
        self.__nb_e_mail=val
        
    @property
    def nb_dir_numero(self) :
        return self.__nb_dir_numero
    
    @nb_dir_numero.setter
    def nb_dir_numero(self, val):
        self.__nb_dir_numero=val
            
    @property
    def nb_dir_colonia(self):
        return self.__nb_dir_colonia    
   
    @nb_dir_colonia.setter
    def nb_dir_colonia(self, val):
        self.__nb_dir_colonia=val
        
    @property
    def cd_dir_cp(self):
        return self.__cd_dir_cp
    
    @cd_dir_cp.setter
    def cd_dir_cp(self, val):
        self.__cd_dir_cp=val
     
    @property
    def nb_dir_estado(self):
        return self.__nb_dir_estado

    @nb_dir_estado.setter
    def nb_dir_estado(self, val):
        self.__nb_dir_estado=val
    
    @property
    def nb_dir_ciudad(self):
        return self.__nb_dir_ciudad
    
    @nb_dir_ciudad.setter
    def nb_dir_ciudad(self, val):
        self.__nb_dir_ciudad
        
    @property
    def nb_txt_adr(self):
        return self.__nb_txt_adr
    
    @nb_txt_adr.setter
    def nb_txt_adr(self, val):
        self.__nb_txt_adr = val        
    
    @property
    def nb_des_comprcty(self) :
        return self.__nb_des_comprcty
    
    @nb_des_comprcty.setter
    def nb_des_comprcty(self,val):
        self.__nb_des_comprcty = val
    
    @property
    def fh_alta_cliente(self):
        return self.__fh_alta_cliente 
    
    @fh_alta_cliente.setter
    def fh_alta_cliente(self,val):
        self.__fh_alta_cliente = val
    
    @property
    def fh_alta_bazdig(self):
        return self.__fh_alta_bazdig
    
    @fh_alta_bazdig.setter
    def fh_alta_bazdig(self,val):
        self.__fh_alta_bazdig=val    
        
    @property
    def fh_alta_superapp(self):
        return self.__fh_alta_superapp                  
    
    @fh_alta_superapp.setter
    def fh_alta_superapp(self,val):
        self.__fh_alta_superapp=val
        
    @property
    def fh_ult_traspasos(self):
        return self.__fh_ult_traspasos
    
    @fh_ult_traspasos.setter
    def fh_ult_traspasos(self,val):
        self.__fh_ult_traspasos =val
        
    @property
    def fh_ult_speis(self):
        return self.__fh_ult_speis
    
    @fh_ult_speis.setter
    def fh_ult_speis(self,val):
        self.fh_ult_speis= val
                 
    @property
    def fh_ult_ret_suc(self):
        return self.__fh_ult_ret_suc
   
    @fh_ult_ret_suc.setter
    def fh_ult_ret_suc(self, val):
        self.__fh_ult_ret_suc = val
    
    @property
    def fh_ult_qr_caja(self):
        return self.__fh_ult_qr_caja
    
    @fh_ult_qr_caja.setter
    def fh_ult_qr_caja(self, val):
        self.__fh_ult_qr_caja=val
        
    @property
    def fh_ult_qr_atm(self):
        return self.__fh_ult_qr_atm
    
    @fh_ult_qr_atm.setter
    def fh_ult_qr_atm(self, val):
        self.__fh_ult_qr_atm=val
        
    @property
    def fh_ult_mod_dermo(self):
        return self.__fh_ult_mod_dermo
    
    @fh_ult_mod_dermo.setter
    def fh_ult_mod_dermo(self, val):
        self.__fh_ult_mod_dermo=val
                     
    @property
    def fh_mod_email(self):
        return self.__fh_mod_email
    
    @fh_mod_email.setter
    def fh_mod_email(self, val):
        self.__fh_mod_email=val
                         
    @property
    def fh_mod_telefono(self):
        return self.__fh_mod_telefono
    
    @fh_mod_telefono.setter
    def fh_mod_telefono(self, val):
       self.__fh_mod_telefono=val
                         
    @property
    def fh_mod_biometricos(self):
        return self.__fh_mod_telefono
    
    @fh_mod_biometricos.setter
    def fh_mod_biometricos(self, val):
        self.__fh_mod_biometricos
    
    @property
    def tp_registro(self):
        return self.__tp_registro
    
    @tp_registro.setter
    def tp_registro(self, val):
        self.__tp_registro = val
        
        
 
 
#c2 = Cliente ( 12902020, 1, "PR" ,"SUC 1" , 120986 ,9876543 ,2345678 , "GOMEZ",
#                "nichteer", "mauricvio" , "1" ,66666, "M", "24/06/1980", "COL" ,"12RTG9K", "WERTYU98" ,
#                "asd@gmail.com " ,"calle cerrada" , 1 ,"cuajimalpa", "cd_dir_cp" ,"nb_dir_estado" ,"nb_dir_ciudad", 
#                "nb_txt_adr" ,"nb_des_comprcty" , "10/10/2000" ,"10/10/2000", 
#                "10/10/2000", "10/10/2000", "10/10/2000", "10/10/2000" , "10/10/2000",
#                "10/10/2000", "10/10/2000", "10/10/2000", 
#                "10/10/2000","10/10/2000","BAZ_DIG")       

#print(c2)
#print(c2.__dict__)
#c2.nb_ap_paterno="LONDONO"
#c2.nb_ap_matern="GARCIA"
#c2.nb_nombre= "MAURICIO"

#print(c2.__dict__)
