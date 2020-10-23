difference(){
    sphere(r=10, $fn=100);
    union(){
        translate(v=[0, 0, 10]){
            sphere(r=5, $fn=100);
        };
        translate(v=[0, 0, -10]){
            sphere(r=5, $fn=50);
        };
        translate(v=[0, 10, 0]){
            sphere(r=5, $fn=50);
        };
        translate(v=[0, -10, 0]){
            sphere(r=5, $fn=50);
        };
        translate(v=[10, 0, 0]){
            sphere(r=5, $fn=50);
        };
        translate(v=[-10, 0, 0]){
            sphere(r=5, $fn=50);
        };
    };
};
