
import math
import secrets
import string

import streamlit as st


st.set_page_config(
    page_title="Secure Password Generator",
    page_icon="🔐",
    layout="centered"
)


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    pools = []

    if use_upper:
        pools.append(string.ascii_uppercase)

    if use_lower:
        pools.append(string.ascii_lowercase)

    if use_digits:
        pools.append(string.digits)

    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Select at least one character type.")

    if length < len(pools):
        raise ValueError("Password length is too short for your selections.")

    alphabet = "".join(pools)

    # Ensure every selected character type appears at least once.
    password_chars = [secrets.choice(pool) for pool in pools]

    # Fill the remaining positions.
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(alphabet))

    # Securely shuffle the characters.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def estimate_strength(length, alphabet_size):
    # Approximate entropy in bits for a uniformly random password.
    entropy = length * math.log2(alphabet_size)

    if entropy < 40:
        label = "Weak"
    elif entropy < 60:
        label = "Fair"
    elif entropy < 80:
        label = "Strong"
    else:
        label = "Very Strong"

    return entropy, label


# ---------------- PAGE DESIGN ----------------

st.title("🔐 Secure Password Generator")
st.write(
    "Generate random passwords and get an estimate "
    "of their strength."
)

st.divider()

st.subheader("Customize your password")

length = st.slider(
    "Password length",
    min_value=4,
    max_value=64,
    value=16
)

col1, col2 = st.columns(2)

with col1:
    use_upper = st.checkbox("Uppercase (A-Z)", value=True)
    use_lower = st.checkbox("Lowercase (a-z)", value=True)

with col2:
    use_digits = st.checkbox("Numbers (0-9)", value=True)
    use_symbols = st.checkbox("Symbols (!@#...)", value=True)

st.caption("For better security, prefer longer, unique passwords.")

if st.button("Generate Password", type="primary", width="stretch"):
    pools = []

    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        st.error("Select at least one character type.")
        st.session_state.pop("password", None)

    elif length < len(pools):
        st.error("Increase the length to fit your selected character types.")
        st.session_state.pop("password", None)

    else:
        st.session_state.password = generate_password(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols
        )

        st.session_state.alphabet_size = len(
            "".join(pools)
        )

if "password" in st.session_state:
    password = st.session_state.password
    alphabet_size = st.session_state.alphabet_size

    st.divider()
    st.subheader("Your generated password")

    # Streamlit's code block provides a copy button.
    st.code(password, language=None)

    entropy, strength = estimate_strength(
        len(password),
        alphabet_size
    )

    st.subheader("Password strength")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Strength estimate", strength)

    with col2:
        st.metric("Estimated entropy", f"{entropy:.1f} bits")

    st.progress(min(entropy / 100, 1.0))

    st.caption(
        "This is an approximate mathematical estimate, "
        "not a guarantee of security. It assumes random generation "
        "and does not account for password exposure or reuse."
    )

    st.success("Password generated successfully!")
