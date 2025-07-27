rule auto_rule_20250727023403_4478 {
  strings:
    $o0 = "dword_44BE5C" wide ascii nocase
  condition:
    all of them
}