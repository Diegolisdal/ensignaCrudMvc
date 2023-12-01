console.log(location.search)     // lee los argumentos pasados a este formulario
var id_plantadoras=location.search.substr(4) // producto_update.html?id=1
var id_tractores=location.search.substr(4)
var id_cosechadoras=location.search.substr(4)  

console.log(id_plantadoras)
const { createApp } = Vue
createApp({
    data() {
        return {
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
            url_plantadoras:'https://diegolis3.pythonanywhere.com/plantadoras/'+id_plantadoras           
       } 
    },
    methods: {
        fetchData(url_plantadoras) {
            fetch(url_plantadoras)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id_plantadoras=data.id_plantadoras
                    this.modelo_plantadora = data.modelo_plantadora
                    this.nroDeLineas_plantadora=data.nroDeLineas_plantadora
                    this.anchoDeLabor_plantadora=data.anchoDeLabor_plantadora
                    this.cajaCentral_plantadora=data.cajaCentral_plantadora
                    this.deslingue_plantadora=data.deslingue_plantadora
                    this.tasaVariable_plantadora=data.tasaVariable_plantadora
                    this.transporte_plantadora=data.transporte_plantadora                    
                    this.imagen_plantadora=data.imagen_plantadora
                    this.stock_plantadora=data.stock_plantadora                                                         
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar_plantadora() {
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
                body: JSON.stringify(plantadora),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_plantadoras, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "./administrador.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url_plantadoras)
    },
}).mount('#app')

/*console log tractores */
console.log(id_tractores)
const { createApp1 } = Vue
createApp1({
    data() {
        return {
            id_tractores:0,                     
            url_tractores:'https://diegolis3.pythonanywhere.com/tractores/'+id_tractores,       
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
                    console.log(data)
                    this.id_tractores=data.id_tractores
                    this.modelo_tractor = data.modelo_tractor
                    this.motor_tractor=data.motor_tractor
                    this.potencia_tractor=data.potencia_tractor
                    this.transmision_tractor=data.transmision_tractor
                    this.toma_tractor=data.toma_tractor
                    this.sistema_tractor=data.sistema_tractor
                    this.levante_tractor=data.levante_tractor                    
                    this.imagen_tractor=data.imagen_tractor
                    this.stock_tractor=data.stock_tractor                                                         
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar_tractor() {
            let plantadora = {
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
                body: JSON.stringify(tractor),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_tractores, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "./administrador.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url_tractores)
    },
}).mount('#app')

/*console log cosechadoras */
console.log(id_plantadoras)
const { createApp2 } = Vue
createApp2({
    data() {
        return {             
            id_cosechadoras:0,                      
            url_cosechadoras:'https://diegolis3.pythonanywhere.com/cosechadoras/'+id_cosechadoras,   // si ya lo subieron a pythonanywhere                                
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
                    console.log(data)
                    this.id_cosechadoras=data.id_cosechadoras
                    this.modelo_cosechadora = data.modelo_cosechadora
                    this.motor_cosechadora=data.motor_cosechadora
                    this.potencia_cosechadora=data.potencia_cosechadora
                    this.plataforma_cosechadora=data.plataforma_cosechadora
                    this.capacidadTolva_cosechadora=data.capacidadTolva_cosechadora
                    this.PilotoAuto_cosechadora=data.PilotoAuto_cosechadora
                    this.jdlink_cosechadora=data.jdlink_cosechadora                    
                    this.combine_cosechadora=data.combine_cosechadora
                    this.activeyield_cosechadora=data.activeyield_cosechadora
                    this.imagen_cosechadora=data.imagen_cosechadora
                    this.stock_cosechadora=data.stock_cosechadora
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar_cosechadora() {
            let cosechadora = {
                modelo_cosechadora:this.modelo_cosechadora,
                motor_cosechadora:this.motor_cosechadora,
                potencia_cosechadora:this.potencia_cosechadora,
                plataforma_cosechadora:this.plataforma_cosechadora,
                capacidadTolva_cosechadora:this.capacidadTolva_cosechadora,
                PilotoAuto_cosechadora:this.PilotoAuto_cosechadora,
                jdlink_cosechadora:this.jdlink_cosechadora,
                combine_cosechadora:this.combine_cosechadora,
                activeyield_cosechadora:this.activeyield_cosechadora,
                imagen_cosechadora:this.imagen_cosechadora, 
                stock_cosechadora:this.stock_cosechadora                 
            }
            var options = {
                body: JSON.stringify(cosechadora),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url_cosechadoras, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "./administrador.html"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url_cosechadoras)
    },
}).mount('#app')