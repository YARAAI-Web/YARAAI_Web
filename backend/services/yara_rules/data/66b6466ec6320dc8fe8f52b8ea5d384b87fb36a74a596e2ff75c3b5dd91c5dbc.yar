rule auto_rule_20250726213910_4445 {
  strings:
    $o0 = "Handler" wide ascii nocase
    $o1 = "_CrtDbgReport" wide ascii nocase
    $o2 = "VirtualFree" wide ascii nocase
  condition:
    3 of ($o*)
}