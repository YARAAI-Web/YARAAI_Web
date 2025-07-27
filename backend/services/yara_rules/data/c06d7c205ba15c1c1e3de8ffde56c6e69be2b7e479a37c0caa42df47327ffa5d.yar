rule auto_rule_20250726091235_0992 {
  strings:
    $o0 = "lpDirectoryName" wide ascii nocase
    $o1 = "idAttachTo" wide ascii nocase
    $o2 = "SetTapePosition" wide ascii nocase
    $o3 = "hConsoleInput" wide ascii nocase
  condition:
    4 of ($o*)
}