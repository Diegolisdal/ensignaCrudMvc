const { createApp } = Vue
createApp({
    data() {
        return {
            plantadoras:[],                        
            url_plantadoras:'https://diegolis3.pythonanywhere.com/plantadoras',
            error_plantadoras:false,
            cargando_plantadoras:true,
            /*atributos para el guardar los valores del formulario */
            id_plantadoras:0,
            modelo_plantadora:"",
            nroDeLineas_plantadora:"",
            anchoDeLabor_plantadora:"",
            cajaCentral_plantadora:"",
            deslingue_plantadora:"",
            tasaVariable_plantadora:"",
            transporte_plantadora:"",
            imagen_plantadora:"",
            stock_plantadora:0,             
        }  
    },
    methods: {
        fetchData(url_plantadoras) {
            fetch(url_plantadoras)
                .then(response => response.json())
                .then(data => {
                    this.plantadoras = data;
                    this.cargando_plantadoras=false
                })
                .catch(err => {
                    console.error(err);
                    this.error_plantadoras=true              
                })
        },
        eliminar_plantadora(id_plantadoras) {
            const url_plantadoras = this.url_plantadoras+'/' + id_plantadoras;
            var options = {
                method: 'DELETE',
            }
            fetch(url_plantadoras, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
			 alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        grabar_plantadora(){
            let plantadora = {                
                modelo_plantadora:this.modelo_plantadora,
                nroDeLineas_plantadora:this.nroDeLineas_plantadora,
                anchoDeLabor_plantadora:this.anchoDeLabor_plantadora,
                cajaCentral_plantadora:this.cajaCentral_plantadora,
                deslingue_plantadora:this.deslingue_plantadora,
                tasaVariable_plantadora:this.tasaVariable_plantadora,
                transporte_plantadora:this.transporte_plantadora,
                imagen_plantadora:this.imagen_plantadora,
                stock_plantadora:this.stock_plantadora
            }
            var options = {
                body:JSON.stringify(plantadora),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_plantadoras, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./administrador.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                })      
        },   
    },
    created() {
        this.fetchData(this.url_plantadoras)     
    },
  }).mount('#app')

  /*tractores */
const { createApp1 } = Vue
createApp1({
    data() {
        return {              
            tractores:[],
            id_tractores:0,             
            url_tractores:'https://diegolis3.pythonanywhere.com/tractores',              
            error_tractores:false,
            cargando_tractores:true,              
            /*atributos para el guardar los valores del formulario */              
            modelo_tractor:"",
            motor_tractor:"",
            potencia_tractor:"",
            transmision_tractor:"",
            toma_tractor:"",
            sistema_tractor:"",
            levante_tractor:"",
            imagen_tractor:"",
            stock_tractor:0
        }  
    },
    methods: {        
        fetchData(url_tractores) {
            fetch(url_tractores)
                .then(response => response.json())
                .then(data => {
                    this.tractores = data;
                    this.cargando_tractores=false
                })
                .catch(err => {
                    console.error(err);
                    this.error_tractores=true              
                })
        },  
        eliminar_tractor(id_tractores) {
            const url_tractores = this.url_tractores+'/' + id_tractores;
            var options = {
                method: 'DELETE',
            }
            fetch(url_tractores, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
            alert('Registro Eliminado')
                location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        grabar_tractor(){
            let tractor = {                
                modelo_tractor:this.modelo_tractor,
                motor_tractor:this.motor_tractor,
                potencia_tractor:this.potencia_tractor,
                transmision_tractor:this.transmision_tractor,
                toma_tractor:this.toma_tractor,
                sistema_tractor:this.sistema_tractor,
                levante_tractor:this.levante_tractor,
                imagen_tractor:this.imagen_tractor,
                stock_tractor:this.stock_tractor
            }
            var options = {
                body:JSON.stringify(tractor),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_tractores, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./administrador.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                })      
        },       
    },
    created() {          
        this.fetchData(this.url_tractores)          
    },
}).mount('#app')
  
  /*cosechadoras */
  const { createApp2 } = Vue
createApp2({
    data() {
        return {
            cosechadoras:[],                        
            url_cosechadoras:'https://diegolis3.pythonanywhere.com/cosechadoras',   // si ya lo subieron a pythonanywhere
            error_cosechadoras:false,
            cargando_cosechadoras:true,            
            /*atributos para el guardar los valores del formulario */                       
            id_cosechadoras:0,
            modelo_cosechadora:"",
            motor_cosechadora:"",
            potencia_cosechadora:"",
            plataforma_cosechadora:"",
            capacidadTolva_cosechadora:"",
            CapacidadDescarga_cosechadora:"",
            PilotoAuto_cosechadora:"",
            jdlink_cosechadora:"",
            combine_cosechadora:"",
            activeyield_cosechadora:"",
            imagen_cosechadora:"",
            stock_cosechadora:0
        }  
    },
    methods: {       
        fetchData(url_cosechadoras) {
            fetch(url_cosechadoras)
                .then(response => response.json())
                .then(data => {
                    this.cosechadoras = data;
                    this.cargando_cosechadoras=false
                })
                .catch(err => {
                    console.error(err);
                    this.error_cosechadoras=true              
                })
        },
        eliminar_cosechadora(id_cosechadoras) {
            const url_cosechadoras = this.url_cosechadoras+'/' + id_cosechadoras;
            var options = {
                method: 'DELETE',
            }
            fetch(url_cosechadoras, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
			 alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        grabar_cosechadora(){
            let cosechadora = {                
                modelo_cosechadora:this.modelo_cosechadora,
                motor_cosechadora:this.motor_cosechadora,
                potencia_cosechadora:this.potencia_cosechadora,
                plataforma_cosechadora:this.plataforma_cosechadora,
                capacidadTolva_cosechadora:this.capacidadTolva_cosechadora,
                CapacidadDescarga_cosechadora:this.CapacidadDescarga_cosechadora,
                PilotoAuto_cosechadora:this.PilotoAuto_cosechadora,
                jdlink_cosechadora:this.jdlink_cosechadora,
                combine_cosechadora:this.combine_cosechadora,
                activeyield_cosechadora:this.activeyield_cosechadora,
                imagen_cosechadora:this.imagen_cosechadora,
                stock_cosechadora:this.stock_cosechadora
            }
            var options = {
                body:JSON.stringify(cosechadora),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_cosechadoras, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "./administrador.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")  // puedo mostrar el error tambien
                })      
        },         
    },
    created() {       
        this.fetchData(this.url_cosechadoras)
    },
  }).mount('#app')
