/**
 * Created by konstantin on 26.01.16.
 */

function hello (){
    var t = $('.dropdown.hello')[0];
    t.remove();
    $('#hello').append(t)

    var q = $('.dropdown-toggle')[0];
    q.style('display: none')

}