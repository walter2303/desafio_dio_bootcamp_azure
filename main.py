import streamlit as st

# Função para armazenar os posts
if 'posts' not in st.session_state:
    st.session_state.posts = []

# Função para adicionar posts
def add_post():
    title = st.text_input('Título do Post')
    content = st.text_area('Conteúdo do Post')

    if st.button('Adicionar Post'):
        if title and content:
            st.session_state.posts.append({'title': title, 'content': content})
            st.success(f'Post "{title}" adicionado com sucesso!')
        else:
            st.error('Por favor, preencha todos os campos.')

# Função para exibir os posts
def display_posts():
    if st.session_state.posts:
        st.write("### Posts Recentes")
        for post in st.session_state.posts:
            st.write(f"#### {post['title']}")
            st.write(post['content'])
            st.markdown("---")
    else:
        st.write("Nenhum post foi adicionado ainda.")

# Título do blog
st.title("Blog Pessoal")

# Adicionar Post
add_post()

# Exibir Posts
display_posts()

