Change Log
##########

..
   All enhancements and patches to hyperpay will be documented
   in this file.  It adheres to the structure of https://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (https://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
**********

Fixed
=====

* MADA payments were verified with the card entity, so HyperPay could not find them: the learner was
  charged but never enrolled. Return and status URLs now carry the processor slug
  (``/hyperpay/<processor>/return/``) and the status check uses that processor's entity. The slug-less
  routes stay for checkouts created before this change.
* A bank-declined payment raised in ``get_checkout_status`` and showed the generic error page. Processed
  payments are now returned for classification, so the learner gets the "declined, no charges were made"
  message and the cart is cancelled.

0.1.1 – 2025-11-30
**********************************************

Added
=====

* hyperpay!

0.1.0 – 2025-09-17
**********************************************

Added
=====

* First release.
