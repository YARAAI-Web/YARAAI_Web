rule auto_rule_20250726114639_7546 {
  strings:
    $o0 = "byte_44F1C0" wide ascii nocase
    $o1 = "dword_45D520" wide ascii nocase
    $o2 = "x140u" wide ascii nocase
  condition:
    3 of ($o*)
}