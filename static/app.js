new Vue({
    el: '#skus_app',
    data: {
        skus:[]
    },
    created: function (){
        const vm = this;
        axios.get('/api/skus/')
            .then(function (response){
                // vm.skus = response.data
                console.log(response.data)
            })

    }
})