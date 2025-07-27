rule auto_rule_20250727024901_2883 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
    $o2 = "dword_44C12C" wide ascii nocase
    $o3 = "ActiveWindow" wide ascii nocase
  condition:
    4 of ($o*)
}