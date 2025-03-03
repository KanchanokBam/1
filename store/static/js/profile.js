document.addEventListener("DOMContentLoaded", function () {
    let profileImageInput = document.getElementById("profileImageInput");
    let avatarPreview = document.getElementById("avatarPreview");

    profileImageInput.addEventListener("change", function () {
        let file = profileImageInput.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (e) {
                avatarPreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
