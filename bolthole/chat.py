# bolthole Orchestrated gRPC chat
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import bolthole_pb2_grpc

# Define max queue size (zero or less is infinite)
__MAX_QUEUE_SIZE__ = 0


class ChatServicer(bolthole_pb2_grpc.ChatServicer):
    """Class to handle the Chat service implementation

    Attributes
    ----------
    __queues__ : list with users chat history queues

    Methods
    -------
    __init__(self) : Constructor
    """

    def __init__(self):
        """Constructor
        """
        # Initialize queues
        self.__queues__ = []
