rule auto_rule_20250726143829_0439 {
  strings:
    $o0 = "stdargv" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "byte_40DCB8" wide ascii nocase
  condition:
    3 of ($o*)
}