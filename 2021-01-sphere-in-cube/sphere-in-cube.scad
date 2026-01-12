union(){
    difference(){
        translate(v=[-10, -10, -10]){
            cube(size=[20, 20, 20]);
        };
        union(){
            translate(v=[6, 2, 2]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
            translate(v=[-6, 2, 2]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
            translate(v=[2, 6, 2]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
            translate(v=[2, -6, 2]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
            translate(v=[2, 2, 6]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
            translate(v=[2, 2, -6]){
                translate(v=[-10, -10, -10]){
                    cube(size=[16, 16, 16]);
                };
            };
        };
    };
    sphere(r=10);
};
