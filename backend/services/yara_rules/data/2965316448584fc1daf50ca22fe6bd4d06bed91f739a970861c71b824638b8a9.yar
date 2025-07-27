rule auto_rule_20250726161856_0578 {
  strings:
    $o0 = "RtlProviderNew" wide ascii nocase
    $o1 = "SendSystemW" wide ascii nocase
    $o2 = "xF89C8549" wide ascii nocase
    $o3 = "dword_41B034" wide ascii nocase
    $o4 = "x45D4u" wide ascii nocase
  condition:
    4 of ($o*)
}