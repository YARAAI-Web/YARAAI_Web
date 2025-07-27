rule auto_rule_20250727023921_2025 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "dword_45CEF0" wide ascii nocase
  condition:
    all of them
}