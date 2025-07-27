rule auto_rule_20250726215421_9757 {
  strings:
    $o0 = "xDF5478985D5D0546uLL" wide ascii nocase
    $o1 = "x10656638CDD875B6LL" wide ascii nocase
  condition:
    all of them
}