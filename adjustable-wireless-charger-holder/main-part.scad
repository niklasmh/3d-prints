difference(){
    union(){
        cube(size=[110.0, 10.0, 10.0]);
        cube(size=[10.0, 10.0, 56.0]);
        translate(v=[0, 0, 46.0]){
            cube(size=[10.0, 20.0, 10.0]);
        };
        translate(v=[0, 10.0, 56.0]){
            cube(size=[10.0, 10.0, 56.5]);
        };
        translate(v=[100.0, 0, 0]){
            cube(size=[10.0, 10.0, 56.0]);
        };
        translate(v=[100.0, 0, 46.0]){
            cube(size=[10.0, 20.0, 10.0]);
        };
        translate(v=[100.0, 10.0, 56.0]){
            cube(size=[10.0, 10.0, 56.5]);
        };
        translate(v=[0, 20.0, 46.0]){
            cube(size=[110.0, 10.0, 66.5]);
        };
        translate(v=[55.0, 10.0, 90.0]){
            rotate(a=[-90, 0, 0]){
                cylinder(h=10.0, r=45.0);
            };
        };
    };
    union(){
        translate(v=[-0.625, 15.0, 51.0]){
            rotate(a=[0, 90, 0]){
                cylinder(h=11.25, r=2.5);
            };
        };
        translate(v=[0, 0, 10.0]){
            translate(v=[-0.625, 15.0, 51.0]){
                rotate(a=[0, 90, 0]){
                    cylinder(h=11.25, r=2.5);
                };
            };
        };
        translate(v=[0, 0, 20.0]){
            translate(v=[-0.625, 15.0, 51.0]){
                rotate(a=[0, 90, 0]){
                    cylinder(h=11.25, r=2.5);
                };
            };
        };
        translate(v=[0, 0, 30.0]){
            translate(v=[-0.625, 15.0, 51.0]){
                rotate(a=[0, 90, 0]){
                    cylinder(h=11.25, r=2.5);
                };
            };
        };
        translate(v=[0, 0, 40.0]){
            translate(v=[-0.625, 15.0, 51.0]){
                rotate(a=[0, 90, 0]){
                    cylinder(h=11.25, r=2.5);
                };
            };
        };
        translate(v=[100.0, 0, 0]){
            union(){
                translate(v=[-0.625, 15.0, 51.0]){
                    rotate(a=[0, 90, 0]){
                        cylinder(h=11.25, r=2.5);
                    };
                };
                translate(v=[0, 0, 10.0]){
                    translate(v=[-0.625, 15.0, 51.0]){
                        rotate(a=[0, 90, 0]){
                            cylinder(h=11.25, r=2.5);
                        };
                    };
                };
                translate(v=[0, 0, 20.0]){
                    translate(v=[-0.625, 15.0, 51.0]){
                        rotate(a=[0, 90, 0]){
                            cylinder(h=11.25, r=2.5);
                        };
                    };
                };
                translate(v=[0, 0, 30.0]){
                    translate(v=[-0.625, 15.0, 51.0]){
                        rotate(a=[0, 90, 0]){
                            cylinder(h=11.25, r=2.5);
                        };
                    };
                };
                translate(v=[0, 0, 40.0]){
                    translate(v=[-0.625, 15.0, 51.0]){
                        rotate(a=[0, 90, 0]){
                            cylinder(h=11.25, r=2.5);
                        };
                    };
                };
            };
        };
    };
    union(){
        translate(v=[110.0, 0, 0]){
            translate(v=[-5.0, 5.0, 5.0]){
                rotate(a=[0, 90, 0]){
                    cylinder(h=10.0, r=2.5);
                };
            };
        };
        translate(v=[-5.0, 5.0, 5.0]){
            rotate(a=[0, 90, 0]){
                cylinder(h=10.0, r=2.5);
            };
        };
    };
};
