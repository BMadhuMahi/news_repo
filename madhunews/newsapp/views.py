from django.shortcuts import render

# Create your views here.
def fun(req):
    head="Wecome to MADHU NEWS portal"
    my_dict={"head":head}
    return render(req,"newsapp/result.html",context=my_dict)
def fun1(req):
    msg="Movies Information"
    msg1="Fida is best and family blockbuster movie"
    msg2="Love story is a very thrilling movie and climax is outstanding acting by saipallavi"
    msg3="Natural star and sai acting in shyamsingoroy movie outstanding"
    type="movies"
    my_dict={"msg":msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,"type":type}

    return render(req,"newsapp/news.html",context=my_dict)
def fun2(req):
    msg="sports Information"
    msg1="India is hatric winner in kabaddi"
    msg2="Tomarrow there is no matches"
    msg3="valloy ball is my second favarite game"
    type="sports"
    my_dict={"msg":msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,"type":type}

    return render(req,"newsapp/news.html",context=my_dict)
def fun3(req):
    msg="politics Information"
    msg1="India PM is Narendar modi"
    msg2="Andra pradesh CM is our Maama Jagan"
    msg3="Telangana CM is Revanth Reddy"
    type="politics"
    my_dict={"msg":msg,"msg1":msg1,"msg2":msg2,"msg3":msg3,"type":type}

    return render(req,"newsapp/news.html",context=my_dict)
