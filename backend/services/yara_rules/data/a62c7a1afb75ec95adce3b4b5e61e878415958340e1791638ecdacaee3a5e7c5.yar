rule auto_rule_20250726132327_2035 {
  strings:
    $o0 = "DefineDosDeviceW" wide ascii nocase
    $o1 = "lpBytesPerSector" wide ascii nocase
    $o2 = "nStdHandle" wide ascii nocase
  condition:
    3 of ($o*)
}