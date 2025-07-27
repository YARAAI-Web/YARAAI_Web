rule auto_rule_20250727023544_8443 {
  strings:
    $o0 = "dword_466AD4" wide ascii nocase
    $o1 = "Addend" wide ascii nocase
  condition:
    all of them
}