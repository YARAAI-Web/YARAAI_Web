rule auto_rule_20250727040205_2093 {
  strings:
    $o0 = "aClasses" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
    $o2 = "dword_4012F4" wide ascii nocase
  condition:
    3 of ($o*)
}