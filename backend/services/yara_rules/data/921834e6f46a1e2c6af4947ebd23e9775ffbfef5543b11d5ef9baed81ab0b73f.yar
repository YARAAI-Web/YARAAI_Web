rule auto_rule_20250726080821_0200 {
  strings:
    $o0 = "nBufferSize" wide ascii nocase
    $o1 = "dword_422BAC" wide ascii nocase
  condition:
    all of them
}