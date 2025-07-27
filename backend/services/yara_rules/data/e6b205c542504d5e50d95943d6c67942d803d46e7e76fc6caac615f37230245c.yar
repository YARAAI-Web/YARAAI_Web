rule auto_rule_20250727015809_0209 {
  strings:
    $o0 = "word_40A548" wide ascii nocase
    $o1 = "word_40A574" wide ascii nocase
    $o2 = "dword_409170" wide ascii nocase
    $o3 = "__crtExitProcess" wide ascii nocase
  condition:
    4 of ($o*)
}