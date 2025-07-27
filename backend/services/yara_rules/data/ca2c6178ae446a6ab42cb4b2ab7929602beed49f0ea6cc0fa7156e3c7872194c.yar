rule auto_rule_20250726062009_6126 {
  strings:
    $o0 = "dword_4309C8" wide ascii nocase
    $o1 = "dword_457440" wide ascii nocase
    $o2 = "lpbi" wide ascii nocase
    $o3 = "RtlUnwind" wide ascii nocase
    $o4 = "dodwords" wide ascii nocase
  condition:
    4 of ($o*)
}