class Pass(object):
        def Valida_Pass(self,pass_r):
            if len(pass_r) >=8 :
                if pass_r.islower()== False:
                    if pass_r.isupper() == False:
                            self.pass_ok = pass_r
                            print("OK!!")
            else:
                print("la contraseña debe tener almenos 8 caracteres")
        
obj = Pass()
contraseña = str(input("ingrese contraseña: "))
print(obj.Valida_Pass(contraseña))
