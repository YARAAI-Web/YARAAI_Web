rule auto_rule_20250727015239_7685 {
  strings:
    $o0 = "off_478FF4" wide ascii nocase
    $o1 = "__heap_select" wide ascii nocase
  condition:
    all of them
}