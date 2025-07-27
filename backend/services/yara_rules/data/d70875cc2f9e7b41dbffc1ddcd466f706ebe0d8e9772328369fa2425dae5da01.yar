rule auto_rule_20250727023352_7817 {
  strings:
    $o0 = "dword_640303E4" wide ascii nocase
  condition:
    all of them
}