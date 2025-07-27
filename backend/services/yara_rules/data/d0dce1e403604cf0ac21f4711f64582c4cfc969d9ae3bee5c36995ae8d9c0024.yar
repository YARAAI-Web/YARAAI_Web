rule auto_rule_20250726072930_9700 {
  strings:
    $o0 = "byte_44B7C8" wide ascii nocase
    $o1 = "auxGetVolume" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
  condition:
    3 of ($o*)
}