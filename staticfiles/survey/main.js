console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const time = modalBtn.getAttribute('data-time')
    const details = modalBtn.getAttribute('data-details')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>details: <b>${details}</b></li>
                <li>number of questions: <b>${numQuestions}</b></li>
                <li>time: <b>${time} min</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))