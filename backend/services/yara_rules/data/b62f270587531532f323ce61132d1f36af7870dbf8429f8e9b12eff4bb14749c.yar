rule auto_rule_20250727023002_5185 {
  strings:
    $o0 = "dword_7A8604" wide ascii nocase
    $o1 = "dword_7A8540" wide ascii nocase
    $o2 = "word_7B4000" wide ascii nocase
    $o3 = "xFFFFFFF7" wide ascii nocase
  condition:
    4 of ($o*)
}