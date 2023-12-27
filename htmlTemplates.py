css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt98d8a946b63c9b5f/64b7170ab314c94aa481d8c3/Untitled_design_(1).jpg?width=850&auto=webp&quality=95&format=jpg&disable=upscale">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://assets.stickpng.com/images/585e4bc4cb11b227491c3395.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''