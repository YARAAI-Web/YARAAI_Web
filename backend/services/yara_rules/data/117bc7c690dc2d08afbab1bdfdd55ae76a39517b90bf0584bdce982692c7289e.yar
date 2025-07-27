rule auto_rule_20250726081026_0534 {
  strings:
    $o0 = "RtlUnwind" wide ascii nocase
    $o1 = "dword_471A74" wide ascii nocase
    $o2 = "off_472064" wide ascii nocase
  condition:
    3 of ($o*)
}