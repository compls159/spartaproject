<script>

    let maxAppend = 1;

    function plus() {
        let temp_button = `<button class='btn' data-bs-toggle='modal' data-bs-target='#exampleModal'><img src='/static/img/timerButton.png'></button>`
        $("#boxWrap").append(temp_button);
        maxAppend++;


    }

    function minus() {
        $("#boxWrap > button").last().remove();
        alert("삭제되었습니다.")
    }

    onscroll = function () {
        var nVScroll = document.documentElement.scrollTop || document.body.scrollTop;
        if (nVScroll >= 0) $(".PMbtn").css("position", "fixed");
        else
            $(".PMbtn").css("position", "relative");
    };

</script>



<script> //메뉴바 작업
   $(document).ready(function () {
        $("#btn_Main").click(function () {
            $.ajax({
                url: "/",
                success: function (data) {
                    $("mainPage").html(data);
                }
            })
        })
    })
    $(document).ready(function () {
        $("#btn_menuTimer").click(function () {
            $.ajax({
                url: "/item",
                success: function (data) {
                    $("itemPage").html(data);
                }
            })
        })
    })
    $(document).ready(function () {
        $("#btn_Login").click(function () {
            $.ajax({
                url: "/login",
                success: function (data) {
                    $("loginPage").html(data);
                }
            })
        })
    })
</script>


<script> //모달창 작업
    function postdata() {

        const item_name_give = $(".item_name_box").text()
        const username = $('#username').text().split('님')[0]
        const dday = document.querySelector("#input_type").value;

        $.ajax({
            type: "POST",
            url: "/item/add",
            data: {
                id_give: username,
                item_name_give: item_name_give,
                start_date_give: dday
            }
        })
        alert()
        window.location.reload()
    }


    function midd(item) {
        $('#middle').empty();
        $.ajax({
            type: "GET",
            url: "/item/modalList",
            data: {},
            success: function (response) {
                let list = response["item_lists"];
                let item_img;
                let item_name;
                let item_timer;
                let item_option;
                for (let i = 0; i < list.length; i++) {
                    if (item === list[i]['item_name']) {
                        item_img = list[i]['item_img'];
                        item_name = list[i]['item_name'];
                        item_timer = list[i]['item_timer'];
                        item_option = list[i]['item_place'];
                        let temp_html = `<div class="item_box">
                                            <div class="item_img_box"><a href="#"><img src="${item_img}"></a></div>
                                            <div class="item_name_box">${item_name}</div>
                                        </div>
                                        <div class="item_box">
                                            <div class="item_timer_box"
                                                 style="height: 50%;
                                                 text-align: center;
                                                 padding-top : 75px">추천 주기는 ${item_timer}일 입니다.</div>
                                            <div class="item_SDate_box">
                                                <input id="input_type" class="input_start" type="date" >
                                            </div>
                                        </div>`
                        $('#middle').append(temp_html);
                    }
                }
            }
        })
    }

    function basi(str) {
        if (str === "부엌") {
            $('#basic').empty();
            $.ajax({
                type: "GET",
                url: "/item/modalList",
                data: {},
                success: function (response) {
                    let list = (response)["item_lists"]
                    for (let i = 0; i < list.length; i++) {
                        let place = list[i]['item_place'];
                        if (place === "부엌") {
                            let gu_name = list[i]['item_name'];

                            let temp_html = `<li><button class="dropdown-item" id = "${gu_name}" onclick = "midd(this.id)">${gu_name}</button></li>`
                            $('#basic').append(temp_html)

                        }
                    }
                }
            })
        } else if (str === "침실") {
            $('#basic').empty();
            $.ajax({
                type: "GET",
                url: "/item/modalList",
                data: {},
                success: function (response) {
                    let list = (response)["item_lists"]
                    for (let i = 0; i < list.length; i++) {
                        let place = list[i]['item_place'];
                        if (place === "침실") {
                            let gu_name = list[i]['item_name'];
                            let temp_html = `<li><button class="dropdown-item"id = "${gu_name}" onclick = "midd(this.id)">${gu_name}</button></li>`
                            $('#basic').append(temp_html)

                        }
                    }
                }
            })
        } else if (str === "화장실") {
            $('#basic').empty();
            $.ajax({
                type: "GET",
                url: "/item/modalList",
                data: {},
                success: function (response) {
                    let list = (response)["item_lists"]
                    for (let i = 0; i < list.length; i++) {
                        let place = list[i]['item_place'];
                        if (place === "화장실") {
                            let gu_name = list[i]['item_name'];
                            let temp_html = `<li><button class="dropdown-item"id = "${gu_name}" onclick = "midd(this.id)">${gu_name}</button></li>`
                            $('#basic').append(temp_html)

                        }
                    }
                }
            })
        }
        if (str === "choose") {
            $('#basic').empty();
            $.ajax({
                type: "GET",
                url: "/item/modalList",
                data: {},
                success: function (response) {
                    let list = (response)["item_lists"]
                    for (let i = 0; i < list.length; i++) {
                        let gu_name = list[i]['item_name'];
                        let temp_html = `<li><button class="dropdown-item" id = "${gu_name}" onclick = "midd(this.id)">${gu_name}</button></li>`
                        $('#basic').append(temp_html)
                    }
                }
            })
        }
    }

    $(document).ready(function () {
        $("#btn_Main").click(function () {
            $.ajax({
                url: "/item/Place",
                data: {},
                success: function (data) {
                    let rows = response['doc']
                    console.log(rows)
                }
            })
        })
    })
    $(document).ready(function () {
        $("#btn_menuTimer").click(function () {
            $.ajax({
                url: "/item",
                success: function (data) {
                    $("itemPage").html(data);
                }
            })
        })
    })
    $(document).ready(function () {
        $("#btn_Login").click(function () {
            $.ajax({

                success: function (data) {
                    $("loginPage").html(data);
                }
            })
        })
    })
    $(document).ready(function () {
        showList();
    })

    function showList() {
        username = $('#username').text().split('님')[0]
        $.ajax({
            type: "GET",
            url: `/item/List?username=${username}`,
            data: {},
            success: function (response) {
                let list = response['user_item']
                for (let i = 0; i < list.length; i++) {
                    let item_name = list[i]['item_name']
                    let item_place = list[i]['item_place']
                    let item_timer = list[i]['item_timer']

                    let temp_html = `<li>${item_name}</li>
                                        <li>${item_place}</li>
                                        <li>${item_timer}</li>`
                    $('#boxWrap').append(temp_html)

                }
            }

        })

    }
</script>