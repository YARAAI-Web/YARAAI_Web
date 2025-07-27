rule auto_rule_20250726135447_5362 {
  strings:
    $o0 = "x3272DBu" wide ascii nocase
    $o1 = "hNamedPipe" wide ascii nocase
    $o2 = "x72B4u" wide ascii nocase
  condition:
    3 of ($o*)
}