rule auto_rule_20250727035812_1478 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "xcptlookup" wide ascii nocase
    $o2 = "dword_450020" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}