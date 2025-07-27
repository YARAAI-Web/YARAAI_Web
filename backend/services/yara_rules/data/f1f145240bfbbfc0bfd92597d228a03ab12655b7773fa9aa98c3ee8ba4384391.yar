rule auto_rule_20250727023014_1364 {
  strings:
    $o0 = "dword_4C15F0" wide ascii nocase
    $o1 = "dword_4C125C" wide ascii nocase
  condition:
    all of them
}