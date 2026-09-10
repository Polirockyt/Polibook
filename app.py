import streamlit as st

# Pagina do navegador

st.set_page_config(page_title="PoliBook", page_icon="📚")

# Titulo Principal

st.title("📚PoliBook - Meu organizador de Leituras")
st.write("Bem Vindo ao seu espaço para gerenciar lidos e desejados")

# Inicializa a lista de livros na memória da sessão

if "livros" not in st.session_state:
    st.session_state.livros = []

# Cadastrar novo livro

st.header("Cadastrar Novo Livro")

with st.form("form_livro"):
    titulo = st.text_input("Título do Livro")
    autor = st.text_input("Autor")
    categoria = st.selectbox("Categoria", ["Romance", "Fantasia", "Ficção Científica", "Biografia", "Outros"])
    status = st.radio("Status", ["Quero Ler", "Lendo", "Lido"])
    url_capa = st.text_input("Link da URL da Capa (opcional)")
    comentario = st.text_area("Comentário ou Resenha")
    
    btn_salvar = st.form_submit_button("Salvar Livro")

    if btn_salvar:
        if titulo:
            novo_livro = {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "status": status,
                "capa": url_capa if url_capa else "https://via.placeholder.com/150",
                "comentario": comentario
            }
            st.session_state.livros.append(novo_livro)
            st.success(f"Livro '{titulo}' cadastrado com sucesso!")
        else:
            st.error("Por favor, preencha o título do livro.")

# Exibição final
st.divider()
st.header("Minha Biblioteca")
if not st.session_state.livros:
    st.info("Nenhum livro cadastrado ainda.")
else:
    for livro in st.session_state.livros:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(livro["capa"], width=100)
        with col2:
            st.subheader(livro["titulo"])
            st.caption(f"Autor: {livro['autor']} | Categoria: {livro['categoria']}")
            st.write(f"**Status:** {livro['status']}")
            if livro["comentario"]:
                st.write(f"**Comentário:** {livro['comentario']}")
        st.divider()
        