rule auto_rule_20250726083119_6180 {
  strings:
    $o0 = "CPtoLCID" wide ascii nocase
    $o1 = "start_byte_3" wide ascii nocase
    $o2 = "lStart" wide ascii nocase
    $o3 = "insb" wide ascii nocase
  condition:
    4 of ($o*)
}