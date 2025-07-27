rule auto_rule_20250726092614_7802 {
  strings:
    $o0 = "qword_180012EC0" wide ascii nocase
    $o1 = "dword_180012ED8" wide ascii nocase
  condition:
    all of them
}