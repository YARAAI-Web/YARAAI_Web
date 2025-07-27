rule auto_rule_20250726083340_1633 {
  strings:
    $o0 = "dword_4463B8" wide ascii nocase
    $o1 = "dword_446044" wide ascii nocase
    $o2 = "program" wide ascii nocase
    $o3 = "dword_44602C" wide ascii nocase
  condition:
    4 of ($o*)
}