$(document).ready(function () {
    $('input[type=radio]').change(
        function () {
            var clickedRadio = this;
            var afterClickedRadio = false;
            var before = []

            var radios = document.querySelectorAll('input[type=radio]');

            for (i = 0; i < radios.length; ++i) {
                var radio = radios[i];

                if (radio === clickedRadio) {
                    afterClickedRadio = true;
                    continue;
                }

                if (!afterClickedRadio && clickedRadio.value === 'A' && radio.value === 'A') {
                    radio.checked = true;
                }
                if (afterClickedRadio && clickedRadio.value === 'B' && radio.value === 'B') {
                    radio.checked = true;
                }
            }

            for (j = 0; j < radios.length; ++j) {
                before.push(j);
                var radio = radios[j]
                    if (radio === clickedRadio) {
                        break;
                    }
            }

            for (k = 0; k < before.length - 2; ++k) {
                var radio = radios[k];

                if (clickedRadio.value === 'B' && radio.value === 'A') {
                    radio.checked = true;
                }
            }

        }
    );
});