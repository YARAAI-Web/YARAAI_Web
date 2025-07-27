rule auto_rule_20250726111312_9406 {
  strings:
    $o0 = "JLI_CmdToArgs" wide ascii nocase
    $o1 = "byte_140004068" wide ascii nocase
    $o2 = "JLI_MemAlloc" wide ascii nocase
    $o3 = "_scrt_set_unhandled_exception_filter" wide ascii nocase
  condition:
    4 of ($o*)
}